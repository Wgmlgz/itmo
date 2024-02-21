<script lang="ts">
  import {
    StructuredList,
    StructuredListHead,
    StructuredListRow,
    StructuredListCell,
    StructuredListBody,
    Dropdown,
    Checkbox,
    Button,
    Toggle
  } from 'carbon-components-svelte';
  import NumberInput from './number-input.svelte';
  import Djson from './djson.svelte';

  export let drive: {
    actualPosition: number | null;
    actualVelocity: number | null;
    alState: number | null;
    currentTask: number | null;
    currentTaskState: number | null;
    errorCode: number | null;
    online: number | null;
    pdsState: number | null;
    probe1LimitSwitchIsOpen: number | null;
    probe2LimitSwitchIsOpen: number | null;
  } = {
    actualPosition: null,
    actualVelocity: null,
    alState: null,
    currentTask: null,
    currentTaskState: null,
    errorCode: null,
    online: null,
    pdsState: null,
    probe1LimitSwitchIsOpen: null,
    probe2LimitSwitchIsOpen: null
  };

  let targetPosition: number;
  let velocity: number;
  let acceleration: number;

  export let startMove: (items: {
    targetPosition: number;
    velocity: number;
    acceleration: number;
  }) => any;

  export let units: string;

  type Range = {
    min: number;
    max: number;
    step: number;
    base?: number;
  };
  export let ranges: {
    targetPosition: Range;
    velocity: Range;
    acceleration: Range;
  };
  export let name: string | undefined = undefined;
  export let position_enabled: boolean = true;
</script>

{#if name}
  <h3>
    {name}
  </h3>
{/if}
<div class="flex gap-10">
  <StructuredList>
    <StructuredListHead>
      <StructuredListRow head class="">
        <StructuredListCell class="w-20%" head />
        <StructuredListCell class="w-40%" head>Плановое</StructuredListCell>
        <StructuredListCell class="w-40%" head>Актуальное</StructuredListCell>
      </StructuredListRow>
    </StructuredListHead>
    <StructuredListBody>
      {#if position_enabled}
        <StructuredListRow>
          <StructuredListCell noWrap>Выбор положения</StructuredListCell>
          <StructuredListCell>
            <Dropdown
              selectedId={0}
              items={[
                { id: 0, text: 'Голова/Шея' },
                { id: 1, text: 'Тело' }
              ]}
            />
          </StructuredListCell>
          <StructuredListCell>
            <Dropdown
              selectedId={0}
              items={[
                { id: 0, text: 'Голова/Шея' },
                { id: 1, text: 'Тело' }
              ]}
            />
          </StructuredListCell>
        </StructuredListRow>
      {/if}
      <StructuredListRow>
        <StructuredListCell noWrap>Позиция</StructuredListCell>
        <StructuredListCell>
          <NumberInput bind:value={targetPosition} {...ranges.targetPosition} {units} />
        </StructuredListCell>
        <StructuredListCell>
          <div class="grid grid-cols-2 gap-4">
            <NumberInput readonly value={drive.actualPosition} {units} />
            <NumberInput disabled />
          </div>
        </StructuredListCell>
      </StructuredListRow>
      <StructuredListRow>
        <StructuredListCell noWrap>Скорость</StructuredListCell>
        <StructuredListCell>
          <NumberInput bind:value={velocity} {...ranges.velocity} units="{units}/с" />
        </StructuredListCell>
        <StructuredListCell>
          <div class="grid grid-cols-2 gap-4">
            <NumberInput readonly value={drive.actualVelocity} units="{units}/с" />
          </div>
        </StructuredListCell>
      </StructuredListRow>
      <StructuredListRow>
        <StructuredListCell noWrap>Ускорение</StructuredListCell>
        <StructuredListCell>
          <NumberInput bind:value={acceleration} {...ranges.acceleration} units="{units}/c²" />
        </StructuredListCell>
      </StructuredListRow>
    </StructuredListBody>
  </StructuredList>

  <div class="flex flex-col gap-2">
    <div>
      <Checkbox labelText="по умолчанию" />
    </div>
    <div>
      <Checkbox labelText="по умолчанию" />
    </div>
    <Button
      on:click={() =>
        startMove({
          targetPosition,
          velocity,
          acceleration
        })}>Старт</Button
    >
    <Button>Стоп</Button>
    <Button>Инициализация</Button>
  </div>

  <div class="w-300px">
    <StructuredList>
      <StructuredListHead>
        <StructuredListRow head />
      </StructuredListHead>
      <StructuredListBody>
        <StructuredListRow>
          <StructuredListCell noWrap>Драйвер</StructuredListCell>
          <StructuredListCell>❔</StructuredListCell>
        </StructuredListRow>
        <StructuredListRow>
          <StructuredListCell noWrap>Концевой выключатель 1</StructuredListCell>
          <StructuredListCell>
            {#if drive.probe1LimitSwitchIsOpen == null}
              ❔
            {:else if drive.probe1LimitSwitchIsOpen}
              ✅
            {:else}
              ❌
            {/if}
          </StructuredListCell>
        </StructuredListRow>
        <StructuredListRow>
          <StructuredListCell noWrap>Концевой выключатель 2</StructuredListCell>
          <StructuredListCell>
            {#if drive.probe2LimitSwitchIsOpen == null}
              ❔
            {:else if drive.probe2LimitSwitchIsOpen}
              ✅
            {:else}
              ❌
            {/if}
          </StructuredListCell>
        </StructuredListRow>
        <StructuredListRow>
          <StructuredListCell noWrap>
            <div class="">
              <p>Тормоз</p>

              <Toggle disabled size="sm">
                <span slot="labelA" />
                <span slot="labelB" />
              </Toggle>
            </div>
          </StructuredListCell>
          <StructuredListCell>❔</StructuredListCell>
        </StructuredListRow>
      </StructuredListBody>
    </StructuredList>
  </div>
</div>

<!-- <Djson item={drive} /> -->
