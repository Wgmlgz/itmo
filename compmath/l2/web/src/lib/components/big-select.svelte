<script>
  let buttonProps = {
    class: [$$restProps.class]
  };
  export let selected = false;
</script>

<button
  on:click
  on:mouseenter
  on:mouseleave
  {...buttonProps}
  class="cursor-pointer w-full transition-all duration-200 ease-in-out bg-white hover:bg-slate-50 focus:bg-slate-50 rounded-xl p-8 shadow border-solid border-2 border-[#0000] focus:border-teal-300"
  class:border-teal-300={selected}
>
  <div class="flex gap-8 items-center">
    <slot />
  </div>
</button>
