<script lang="ts">
  import { CheckboxCheckedFilled } from 'carbon-icons-svelte';

  export let text: string | undefined = undefined;
  export let primaryFocus = false;
  export let checked = false;
</script>

<div
  on:click
  class="cursor-pointer border-3px w-full text-left border-# border-solid px-2 flex items-center gap-2"
  style="border-color: {primaryFocus ? '#0f62fe' : '#0000'}"
  on:keydown
  on:keyup
>
  {#if text}
    <p>
      {text}
    </p>
  {/if}
  <slot />

  {#if checked}
    <CheckboxCheckedFilled />
  {/if}
</div>
