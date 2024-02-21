<script>
  let buttonProps = {
    class: [$$restProps.class]
  };
  export let disabled = false;
</script>

<button
  on:click
  on:mouseenter
  on:mouseleave
  {...buttonProps}
  class="cursor-pointer transition-all duration-1000 ease-in-out border-none px-6 py-3 rounded shadow text-center text-white text-lg font-['Inter'] bg-gradient-to-l {disabled
    ? 'from-slate-300 to-slate-300'
    : 'from-teal-500 to-emerald-400'}"
>
  <slot />
</button>
