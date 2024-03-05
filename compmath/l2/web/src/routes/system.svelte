<script lang="ts">
  import { onMount } from 'svelte';
  import {
    Button,
    TextInput,
    Select,
    SelectItem,
    Tile,
    NumberInput,
    FileUploader,
    InlineLoading,
    FileUploaderDropContainer
  } from 'carbon-components-svelte';
  import { fromZodError } from 'zod-validation-error';

  import {
    equations,
    InputSchema,
    type F,
    methods,
    type Solution,
    download,
    SystemInputSchema,
    type F3D,
    systems,
    solve_system,
    type SystemSolution,
    type System
  } from './utils';
  import Katex from './katex.svelte';
  import Plotly, { type PlotData } from 'plotly.js-dist-min';
  import type { z } from 'zod';

  let input: z.infer<typeof SystemInputSchema> = {
    system: 1,
    xs: [1, 1],
    tolerance: 0.01
  };

  let system: System | undefined = undefined;

  const plotSystem3D = async (fs: F3D[], a: number, b: number, points: number = 600) => {
    const x = Array.from({ length: points }, (_, i) => a + (i * (b - a)) / (points - 1));
    const y = Array.from({ length: points }, (_, i) => a + (i * (b - a)) / (points - 1));

    let z = fs.map((f) => {
      let xValues = [];
      let yValues = [];

      for (let j = 0; j < points; j++) {
        for (let i = 0; i < points; i++) {
          const t_x = x[i];
          const t_y = y[j];
          const z = f(t_x, t_y);
          if (Math.abs(z) < 0.05) {
            // Adjust threshold as needed
            xValues.push(t_x);
            yValues.push(t_y);
          }
        }
      }
      return { xValues, yValues };
    });

    const data: Partial<PlotData>[] = z.map(({ xValues, yValues }) => ({
      x: xValues,
      y: yValues,
      mode: 'markers', // This will connect the points with lines
      type: 'scatter',
      line: { shape: 'spline' },
      marker: { size: 3 }
    }));

    const layout = {
      title: 'Система функций',
      xaxis: { title: 'x' },
      yaxis: { title: 'y' },
      autosize: true,
      margin: { l: 65, r: 50, b: 65, t: 90 }
    };

    Plotly.newPlot('plot', data, layout);
  };

  $: if (input.system) system = systems.filter(({ id }) => id === input.system)[0];
  $: if (system && plot) plotSystem3D(system.fs, -6, 6);

  const solve = () => {
    const { xs, tolerance } = input;
    try {
      if (!system) return;
      solution = solve_system(system, xs, tolerance);
      // solution = solver(a, b, tolerance, f);
      err = null;
    } catch (e: any) {
      solution = null;
      err = e.toString();
    }
  };

  let plot: HTMLDivElement;
  let err: string | null = null;

  let solution: SystemSolution | null = null;
  const onFile = (file: File) => {
    var reader = new FileReader();
    reader.onload = function (event: any) {
      try {
        let s = event.target.result;
        let json = JSON.parse(s);
        const validationResult = SystemInputSchema.safeParse(json);

        if (validationResult.success) {
          input = validationResult.data;
          err = null;
        } else {
          const validationError = fromZodError(validationResult.error);
          err = `Ошибка валидации: ${validationError}`;
        }
      } catch (e: any) {
        err = e.toString();
      }
    };
    reader.readAsText(file);
  };
</script>

<Tile>
  <div class="grid grid-cols-2 gap-10">
    <div class="h-700px">
      <div class="h-700px" bind:this={plot} id="plot" />
    </div>

    <div class="grid gap-2 h-min">
      <div class="flex gap-2">
        <Select bind:selected={input.system} labelText="Выберите уравнение">
          {#each systems as { id, tex }}
            <SelectItem value={id} text={tex}>
              <!-- <Katex {tex} /> -->
            </SelectItem>
          {/each}
        </Select>
      </div>
      <div class="flex gap-2">
        <NumberInput step={0.001} label="x" type="number" bind:value={input.xs[0]} />
        <NumberInput step={0.001} label="y" type="number" bind:value={input.xs[1]} />
        <NumberInput step={0.001} label="Точность" type="number" bind:value={input.tolerance} />
      </div>
      <div class="flex gap-2 items-center">
        <div>
          <FileUploaderDropContainer
            labelText="Выбрать файл"
            accept={['.json']}
            on:change={(e) => {
              console.log(e);
              let file = e.detail[0];
              onFile(file);
            }}
          />
        </div>
        <div class="ml-auto">
          <Button size="small" on:click={solve}>Решить</Button>
        </div>
      </div>
      {#if err}
        <InlineLoading status="error" description={err} />
      {/if}
      {#if solution}
        <p>
          xs: {solution.solution.map((x) => x.toFixed(3))}
        </p>
        <p>
          итераций: {solution.iterations}
        </p>

        <p>вектор погрешностей:</p>
        {#each solution.errors as errors}
          <pre>
            {errors.map((x) => x.toFixed(3)).join(' ')}
          </pre>
        {/each}
        <Button
          size="small"
          on:click={() => {
            download(
              'solution.json',
              JSON.stringify(
                {
                  input,
                  solution
                },
                null,
                2
              )
            );
          }}>Сохранить решение</Button
        >
      {/if}
    </div>
  </div>
</Tile>
