import z from 'zod';
const EquationEnum = z.union([
  z.literal(1),
  z.literal(2),
  z.literal(3),
  z.literal(4),
  z.literal(5)
]);
const MethodEnum = z.union([z.literal(2), z.literal(4), z.literal(5)]);

export const InputSchema = z
  .object({
    equation: EquationEnum,
    method: MethodEnum,
    a: z.number(),
    b: z.number(),
    tolerance: z.number().positive('Точность должна быть больше 0') // tolerance > 0
  })
  .refine((data) => data.b > data.a, {
    message: 'b должно быть больше a',
    path: ['b'] // Указываем путь к полю, где произошла ошибка, для более точного сообщения об ошибке
  });

export type F = (x: number) => number;

export type Equation = {
  id: number;
  tex: string;
  f: F;
  f1: F;
  f2: F;
};

export const equations: Equation[] = [
  {
    id: 1,
    tex: 'sin(x) - cos(2x)',
    f: (x) => Math.sin(x) - Math.cos(2 * x),
    f1: (x) => 2 * Math.sin(2 * x) + Math.cos(x),
    f2: (x) => -Math.sin(x) + 4 * Math.cos(2 * x)
  },
  {
    id: 2,
    tex: 'x^4 - 5x^3 + 5x^2 + 5x - 6',
    f: (x) => x ** 4 - 5 * x ** 3 + 5 * x ** 2 + 5 * x - 6,
    f1: (x) => 4 * x ** 3 - 15 * x ** 2 + 10 * x + 5,
    f2: (x) => 12 * x ** 2 - 30 * x + 10
  },
  {
    id: 3,
    tex: 'sin(x) + x^2 - 2',
    f: (x) => Math.sin(x) + x ** 2 - 2,
    f1: (x) => 2 * x + Math.cos(x),
    f2: (x) => 2 - Math.sin(x)
  },
  {
    id: 4,
    tex: 'e^(-x) * sin(5x)',
    f: (x) => Math.exp(-x) * Math.sin(5 * x),
    f1: (x) => -Math.exp(-x) * Math.sin(5 * x) + 5 * Math.exp(-x) * Math.cos(5 * x),
    f2: (x) => -10 * Math.exp(-x) * (Math.sin(5 * x) + 6 * Math.cos(5 * x))
  },
  {
    id: 5,
    tex: 'ln(x) + x^2 - 3',
    f: (x) => Math.log(x) + x ** 2 - 3,
    f1: (x) => 2 * x + 1 / x,
    f2: (x) => 2 - 1 / x ** 2
  }
];

export type Solution = {
  root: number;
  f_x: number;
  f1_x: number;
  f2_x: number;
  iterations: number;
};

type Solver = (a: number, b: number, tolerance: number, { f }: Equation) => Solution;

const chordMethod: Solver = (a: number, b: number, tolerance: number, { f, f1, f2 }: Equation) => {
  // Проверка корректности введённых данных
  if (tolerance <= 0) {
    throw new Error('Точность должна быть больше 0');
  }
  if (a >= b) {
    throw new Error('a должно быть меньше b');
  }
  if (f(a) * f(b) > 0) {
    throw new Error(
      'На интервале отсутствуют или находится несколько корней, f(a) и f(b) должны иметь разные знаки'
    );
  }

  let x = a; // Начальное приближение
  let iterations = 0;

  for (let i = 0; i < 10000; ++i) {
    iterations++;
    const prevX = x;
    x = b - (f(b) * (a - b)) / (f(a) - f(b)); // Вычисление следующего приближения

    if (Math.abs(f(x)) < tolerance || Math.abs(x - prevX) < tolerance) {
      return { root: x, f_x: f(x), f1_x: f1(x), f2_x: f2(x), iterations };
    }

    // Переоценка a и b на основе знака f(x)
    if (f(a) * f(x) < 0) {
      b = x;
    } else {
      a = x;
    }
  }
  throw new Error('Превышено максимальное число итераций');
};

const secantMethod: Solver = (a: number, b: number, tolerance: number, { f, f1, f2 }: Equation) => {
  if (tolerance <= 0) {
    throw new Error('Точность должна быть больше 0');
  }
  if (a >= b) {
    throw new Error('a должно быть меньше b');
  }

  let x0 = a;
  let x1 = b;
  console.log("f(a), f'(a), f''(a)");
  console.log(f(a), f1(a), f2(a));
  console.log("f(b), f'(b), f''(b)");
  console.log(f(b), f1(b), f2(b));

  const e = 0.01;
  if (f(a) * f2(a) > 0) {
    x0 = a;
    x1 = a + e;
  } else if (f(b) * f2(b) > 0) {
    x0 = b;
    x1 = b - e;
    // x1 = (a + b) / 2
  }
  console.log('x0, x1');
  console.log(x0, x1);

  let iterations = 0;

  for (let i = 0; i < 10000; ++i) {
    iterations++;
    const fx0 = f(x0);
    const fx1 = f(x1);
    const x2 = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0); // Вычисление следующего приближения

    if (Math.abs(f(x2)) < tolerance && Math.abs(x2 - x1) < tolerance) {
      console.log('Math.abs(f(x2)) < tolerance');
      console.log(Math.abs(f(x2)) < tolerance);
      console.log('Math.abs(x2 - x1) < tolerance');
      console.log(Math.abs(x2 - x1) < tolerance);
      const x = x2;
      return { root: x2, f_x: f(x), f1_x: f1(x), f2_x: f2(x), iterations };
    }

    x0 = x1; // Обновление предыдущих приближений
    x1 = x2;
  }

  throw new Error('Превышено максимальное число итераций');
};

const simpleIterationMethod: Solver = (
  a: number,
  b: number,
  tolerance: number,
  { f, f1, f2 }: Equation
) => {
  // Проверка корректности введённых данных
  if (tolerance <= 0) {
    throw new Error('Точность должна быть больше 0');
  }
  if (a >= b) {
    throw new Error('a должно быть меньше b');
  }

  let lambda = 1 / Math.max(Math.abs(f1(a)), Math.abs(f1(b)));

  console.log(`f'((a + b) / 2)`);
  console.log(f1((a + b) / 2));

  if (f1((a + b) / 2) > 0) lambda = -lambda;
  console.log('lambda');
  console.log(lambda);

  // Определение функции g(x) для метода простой итерации
  const g = (x: number) => x + lambda * f(x);
  const g1 = (x: number) => 1 + lambda * f1(x);
  console.log(`g'(a)`);
  console.log(g1(a));
  console.log(`g'(b)`);
  console.log(g1(b));

  let x = a; // Начальное приближение
  let iterations = 0;

  for (let i = 0; i < 100; ++i) {
    iterations++;
    const nextX = g(x);
    const error = Math.abs(nextX - x);

    if (error < tolerance) {
      const x = nextX;
      return { root: nextX, f_x: f(x), f1_x: f1(x), f2_x: f2(x), iterations };
    }

    x = nextX;
    console.log(x);
    // if (nextX < a || nextX > b) {
    //   throw new Error('Последовательность выходит за пределы интервала');
    // }
  }

  throw new Error('Превышено максимальное число итераций');
};

export type Method = {
  id: number;
  name: string;
  solver: Solver;
};
export const methods: Method[] = [
  {
    id: 2,
    name: 'метод хорд',
    solver: chordMethod
  },
  {
    id: 4,
    name: 'метод секущих',
    solver: secantMethod
  },
  {
    id: 5,
    name: 'метод простой итерации',
    solver: simpleIterationMethod
  }
];

export function download(filename: string, text: string) {
  const element = document.createElement('a');
  element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
  element.setAttribute('download', filename);

  element.style.display = 'none';
  document.body.appendChild(element);

  element.click();

  document.body.removeChild(element);
}

export type F3D = (x: number, y: number) => number;

export interface IterativeUpdate {
  updateX1: (x: number, y: number) => number;
  updateX2: (x: number, y: number) => number;
}

export type System = {
  id: number;
  tex: string;
  fs: F3D[];
  iterativeUpdates: IterativeUpdate;
  dir: ((x: number, y: number) => number)[];
};
export const systems: System[] = [
  {
    id: 1,
    tex: 'Система 1: 0.1x₁²+x₁+0.2x₂²-0.3=0 и 0.2x₁²+x₂+0.1x₁x₂-0.7=0',
    fs: [
      (x1, x2) => 0.1 * x1 ** 2 + x1 + 0.2 * x2 ** 2 - 0.3,
      (x1, x2) => 0.2 * x1 ** 2 + x2 + 0.1 * x1 * x2 - 0.7
    ],
    iterativeUpdates: {
      updateX1: (x1, x2) => 0.3 - 0.1 * x1 ** 2 - 0.2 * x2 ** 2,
      updateX2: (x1, x2) => 0.7 - 0.2 * x1 ** 2 - 0.1 * x1 * x2
    },
    dir: [
      (x1, x2) => -0.2 * x1,
      (x1, x2) => -0.4 * x2,
      (x1, x2) => -0.4 * x1 - 0.1 * x2,
      (x1, x2) => -0.1 * x1
    ]
  },
  {
    id: 2,
    tex: 'Система 2: sin(x+y)-1.4x=0 и cos(x)-2y=4',
    fs: [(x, y) => Math.sin(x + y) - 1.4 * x, (x, y) => Math.cos(x) - 2 * y - 4],
    iterativeUpdates: {
      updateX1: (x, y) => Math.sin(x + y) / 1.4, // Update x using the current y
      updateX2: (x, y) => (Math.cos(x) - 4) / 2 // Update y using the current x
    },
    dir: []
  },
  {
    id: 3,
    tex: 'Система 3: ln(x)+y=2 и x-2y=0',
    fs: [(x, y) => Math.log(x) + y - 2, (x, y) => x - 2 * y],
    iterativeUpdates: {
      updateX1: (x, y) => 2 * y, // Direct from rearranged x - 2y = 0
      updateX2: (x, y) => 2 - Math.log(x) // Direct from rearranged ln(x) + y = 2
    },
    dir: []
  }
];

const SystemEnum = z.union([z.literal(1), z.literal(2), z.literal(3), z.literal(4), z.literal(5)]);

export const SystemInputSchema = z.object({
  system: SystemEnum,
  xs: z.array(z.number()),
  tolerance: z.number().positive('Точность должна быть больше 0') // tolerance > 0
});

export type SystemSolution = { solution: number[]; iterations: number; errors: number[][] };
export const solve_system = (
  system: System,
  initialApproximations: number[],
  tolerance = 1e-6,
  maxIterations = 100
): SystemSolution => {
  let [x, y] = initialApproximations;
  const errors: number[][] = [];

  // const phi_1 = Math.abs(system.dir[0](x, y)) + Math.abs(system.dir[1](x, y));
  // const phi_2 = Math.abs(system.dir[2](x, y)) + Math.abs(system.dir[3](x, y));

  // console.log('phi_1');
  // console.log(phi_1);
  // console.log('phi_2');
  // console.log(phi_2);
  // if (Math.max(Math.abs(phi_1), Math.abs(phi_2)) > 1) {
  //   console.log('Условие сходимости не соблюдено');
  // }

  for (let i = 0; i < maxIterations; i++) {
    const newX = system.iterativeUpdates.updateX1(x, y);
    const newY = system.iterativeUpdates.updateX2(x, y);

    const errorX = Math.abs(newX - x);
    const errorY = Math.abs(newY - y);
    errors.push([errorX, errorY]);

    x = newX;
    y = newY;
    console.log(x, y);

    if (
      Math.abs(system.fs[0](x, y)) < tolerance &&
      Math.abs(system.fs[1](x, y)) < tolerance
      // &&
      // errorX < tolerance &&
      // errorY < tolerance
    ) {
      const results = system.fs.map((f) => f(x, y));
      console.log(results);
      return { solution: [x, y], iterations: i + 1, errors };
    }
  }

  throw new Error('Превышено максимальное число итераций');
};
