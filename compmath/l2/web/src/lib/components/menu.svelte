<script>
  import { clickOutside } from '$lib/click_outside';
  import OverflowMenuVertical from 'carbon-icons-svelte/lib/OverflowMenuVertical.svelte';

  let expanded = false;
</script>

<div class="relative">
  <div
    class="cursor-pointer h-30px w-20px grid items-center justify-center border-3px border-solid"
    style="border-color: {expanded ? '#0f62fe' : '#0000'}"
    on:click={() => {
      expanded = true;
    }}
    use:clickOutside
    on:outsideClick={() => (expanded = false)}
    on:keydown,
    on:keyup,
    on:keypress
  >
    <OverflowMenuVertical />
  </div>
  {#if expanded}
    <div class="z-10 absolute top-30px left-0 bg-white grid text-left p-1 gap-2 rounded w-max">
      <slot />
    </div>
  {/if}
</div>
