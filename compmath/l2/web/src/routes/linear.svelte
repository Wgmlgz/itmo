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

  import { equations, InputSchema, type F, methods, type Solution, download, type Equation } from './utils';
  import Katex from './katex.svelte';
  import Plotly from 'plotly.js-dist-min';
  import type { z } from 'zod';

  let input: z.infer<typeof InputSchema> = {
    equation: 1,
    method: 2,
    a: 0,
    b: 1,
    tolerance: 0.001
  };

  let eq: Equation | undefined = undefined;

  const plotFunction = async (f: F) => {
    const a = -10;
    const b = 10;
    const x = Array.from({ length: 400 }, (_, i) => a + (i * (b - a)) / 399);
    const y = x.map(f);

    const data = [
      {
        x,
        y
      }
    ];

    const layout = {
      title: 'График функции',
      xaxis: { title: 'x' },
      yaxis: { title: 'f(x)' },
      margin: { t: 40 }
    };

    Plotly.newPlot('plot3', data, layout);
  };
  $: if (input.equation) eq = equations.filter(({ id }) => id === input.equation)[0];
  $: if (eq && plot) plotFunction(eq.f);

  const solve = () => {
    const { solver } = methods.filter(({ id }) => id === input.method)[0];
    const { a, b, tolerance } = input;
    try {
      if (!eq) return;
      solution = solver(a, b, tolerance, eq);
      err = null;
    } catch (e: any) {
      solution = null;
      err = e.toString();
    }
  };

  let plot: HTMLDivElement;
  let err: string | null = null;

  let solution: Solution | null = null;
  const onFile = (file: File) => {
    var reader = new FileReader();
    reader.onload = function (event: any) {
      try {
        let s = event.target.result;
        let json = JSON.parse(s);
        const validationResult = InputSchema.safeParse(json);

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
    <div class="h-500px">
      <div bind:this={plot} id="plot3" />
    </div>

    <div class="grid gap-2 h-min">
      <div class="flex gap-2">
        <Select bind:selected={input.equation} labelText="Выберите уравнение">
          {#each equations as { id, tex }}
            <SelectItem value={id} text={tex}>
              <!-- <Katex {tex} /> -->
            </SelectItem>
          {/each}
        </Select>

        <Select bind:selected={input.method} labelText="Выберите метод">
          {#each methods as { id, name }}
            <SelectItem text={name} value={id} />
          {/each}
        </Select>
      </div>
      <div class="flex gap-2">
        <NumberInput step={0.001} label="Начало интервала" type="number" bind:value={input.a} />
        <NumberInput step={0.001} label="Конец интервала" type="number" bind:value={input.b} />
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
          x: {solution.root.toFixed(3)}, f(x): {solution.f_x}
        </p>
        <p>
          итераций: {solution.iterations}
        </p>
        <Button
          size="small"
          on:click={() => {
            download(
              'solution.json',
              JSON.stringify({
                input,
                solution
              }, null, 2)
            );
          }}>Сохранить решение</Button
        >
      {/if}
    </div>
  </div>
</Tile>
