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
};

export const equations: Equation[] = [
  {
    id: 1,
    tex: 'sin(x) - cos(2x)',
    f: (x) => Math.sin(x) - Math.cos(2 * x)
  },
  {
    id: 2,
    tex: 'x^4 - 5x^3 + 5x^2 + 5x - 6',
    f: (x) => x ** 4 - 5 * x ** 3 + 5 * x ** 2 + 5 * x - 6
  },
  {
    id: 3,
    tex: 'sin(x) + x^2 - 2',
    f: (x) => Math.sin(x) + x ** 2 - 2
  },
  {
    id: 4,
    tex: 'e^(-x) * sin(5x)',
    f: (x) => Math.exp(-x) * Math.sin(5 * x)
  },
  {
    id: 5,
    tex: 'ln(x) + x^2 - 3',
    f: (x) => Math.log(x) + x ** 2 - 3 // Обратите внимание: Math.log() в JavaScript возвращает натуральный логарифм (ln)
  }
];

export type Solution = { root: number; valueAtRoot: number; iterations: number };

type Solver = (a: number, b: number, tolerance: number, f: F) => Solution;

const chordMethod: Solver = (a: number, b: number, tolerance: number, f: F) => {
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
      return { root: x, valueAtRoot: f(x), iterations };
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

const secantMethod: Solver = (a: number, b: number, tolerance: number, f: F) => {
  if (tolerance <= 0) {
    throw new Error('Точность должна быть больше 0');
  }
  if (a >= b) {
    throw new Error('a должно быть меньше b');
  }

  let x0 = a;
  let x1 = b;
  let iterations = 0;

  for (let i = 0; i < 10000; ++i) {
    iterations++;
    const fx0 = f(x0);
    const fx1 = f(x1);
    const x2 = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0); // Вычисление следующего приближения

    if (Math.abs(f(x2)) < tolerance || Math.abs(x2 - x1) < tolerance) {
      return { root: x2, valueAtRoot: f(x2), iterations };
    }

    x0 = x1; // Обновление предыдущих приближений
    x1 = x2;
  }

  throw new Error('Превышено максимальное число итераций');
};

const simpleIterationMethod: Solver = (a: number, b: number, tolerance: number, f: F) => {
  // Проверка корректности введённых данных
  if (tolerance <= 0) {
    throw new Error('Точность должна быть больше 0');
  }
  if (a >= b) {
    throw new Error('a должно быть меньше b');
  }

  // Определение функции g(x) для метода простой итерации
  const g = (x: number) => x - 0.05 * f(x);

  let x = a; // Начальное приближение
  let iterations = 0;

  for (let i = 0; i < 10000; ++i) {
    iterations++;
    const nextX = g(x);
    const error = Math.abs(nextX - x);

    if (error < tolerance) {
      return { root: nextX, valueAtRoot: f(nextX), iterations };
    }

    x = nextX;

    if (nextX < a || nextX > b) {
      throw new Error('Последовательность выходит за пределы интервала');
    }
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

export type System = {
  id: number;
  tex: string;
  fs: F3D[];
};
export const systems: System[] = [
  {
    id: 1,
    tex: 'Система 1: x^2 + y^2 = 4 и e^x + y = 1',
    fs: [(x, y) => x ** 2 + y ** 2 - 4, (x, y) => Math.exp(x) + y - 1]
  },
  {
    id: 2,
    tex: 'Система 2: sin(x) + cos(y) = 0.5 и x^2 + y^2 = 9',
    fs: [(x, y) => Math.sin(x) + Math.cos(y) - 0.5, (x, y) => x ** 2 + y ** 2 - 9]
  },
  {
    id: 3,
    tex: 'Система 3: ln(x) + y = 2 и x - 2y = 0',
    fs: [(x, y) => Math.log(x) + y - 2, (x, y) => x - 2 * y]
  }
];

// Для реализации метода простой итерации для каждой из предложенных систем нелинейных уравнений, нам необходимо преобразовать каждую систему так, чтобы она имела вид подходящий для итеративного процесса: x=g(x,y)x=g(x,y) и y=h(x,y)y=h(x,y). Это потребует некоторого аналитического преобразования уравнений системы для выражения одной переменной через другую и константы.
// Система 1:

// Исходные уравнения:
// x2+y2=4x2+y2=4
// ex+y=1ex+y=1

// Можно преобразовать в следующие функции для итераций:
// g(x,y)=4−y2g(x,y)=4−y2
// (или −4−y2−4−y2

// в зависимости от начального приближения и интересующего нас корня)
// h(x,y)=1−exh(x,y)=1−ex
// Система 2:

// Исходные уравнения:
// sin⁡(x)+cos⁡(y)=0.5sin(x)+cos(y)=0.5
// x2+y2=9x2+y2=9

// Преобразования могут быть следующими:
// g(x,y)=arcsin⁡(0.5−cos⁡(y))g(x,y)=arcsin(0.5−cos(y)) (учитывая область значений sin⁡sin и cos⁡cos)
// h(x,y)=9−x2h(x,y)=9−x2
// (или −9−x2−9−x2

//)
// Система 3:

// Исходные уравнения:
// ln⁡(x)+y=2ln(x)+y=2
// x−2y=0x−2y=0

// Преобразования:
// g(x,y)=2yg(x,y)=2y (прямое следствие второго уравнения)
// h(x,y)=2−ln⁡(x)h(x,y)=2−ln(x)
// Вывод функций g и h для TypeScript:

// typescript

// export const systems: System[] = [
//   {
//     id: 1,
//     tex: 'Система 1: x^2 + y^2 = 4 и e^x + y = 1',
//     g: (x, y) => Math.sqrt(4 - y**2), // или g: (x, y) => -Math.sqrt(4 - y**2)
//     h: (x, y) => 1 - Math.exp(x)
//   },
//   {
//     id: 2,
//     tex: 'Система 2: sin(x) + cos(y) = 0.5 и x^2 + y^2 = 9',
//     g: (x, y) => Math.asin(0.5 - Math.cos(y)), // Учтите область значений и возможность множественных решений
//     h: (x, y) => Math.sqrt(9 - x**2) // или h: (x, y) => -Math.sqrt(9 - x**2)
//   },
//   {
//     id: 3,
//     tex: 'Система 3: ln(x) + y = 2 и x - 2y = 0',
//     g: (x, y) => 2 * y,
//     h: (x, y) => 2 - Math.log(x)
//   }
// ];

// Эти преобразования представляют собой один из возможных способов подготовки систем для метода простой итерации. Важно учитывать область определения функций и выбирать соответствующие ветви функций (например, знак перед корнем) в зависимости от начальных приближений и интересующей области поиска решения.

const SystemEnum = z.union([z.literal(1), z.literal(2), z.literal(3), z.literal(4), z.literal(5)]);

export const SystemInputSchema = z.object({
  system: SystemEnum,
  xs: z.array(z.number()),
  tolerance: z.number().positive('Точность должна быть больше 0') // tolerance > 0
});

export type SystemSolution = { solution: number[]; iterations: number; errors: number[] };
export const solve_system = (
  fs: F3D[],
  xs: number[],
  tolerance = 1e-6,
  maxIterations = 10000
): SystemSolution => {
  let [x, y] = xs;
  const errors = [];

  for (let i = 0; i < maxIterations; i++) {
    const newX = fs[0](x, y);
    const newY = fs[1](x, y);

    const errorX = Math.abs(newX - x);
    const errorY = Math.abs(newY - y);
    errors.push(errorX, errorY);

    x = newX;
    y = newY;
    console.log(x, y);
    if (errorX < tolerance && errorY < tolerance) {
      return { solution: [x, y], iterations: i + 1, errors };
    }
  }

  throw new Error('Превышено максимальное число итераций');
};
