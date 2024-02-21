<script lang="ts">
  export let label = '';
</script>

<div class="flex items-center gap-2">
  {#if label}
    <p>{label}</p>
  {/if}
  <slot />
</div>
