<script lang="ts">
  import { FluidForm, InlineLoading, InlineNotification, Tile } from 'carbon-components-svelte';
  import BigSelect from '$lib/components/big-select.svelte';
  import Button from '$lib/components/button.svelte';
  import { PasswordInput } from 'carbon-components-svelte';
  import { TextInput } from 'carbon-components-svelte';
  import { api } from '$lib/eois';
  import { goto } from '$app/navigation';
  import type { AxiosError } from 'axios';
  import Med from '$lib/icons/med.svelte';
  import Tool from '$lib/icons/tool.svelte';
  import ArrowRightWhite from '$lib/icons/arrow-right-white.svelte';

  let selected: string = '';
</script>

<div class="w-screen h-screen flex">
  <div class="w-6/16 h-full relative">
    <img class="w-full h-full absolute object-cover" src="images/doctor-back.jpg" alt="doctor" />
    <div
      class="w-full h-full opacity-67% absolute top-0 left-0 bg-gradient-to-l from-teal-500 to-emerald-400"
    />
  </div>
  <div class="grid place-items-center w-10/16 px-10">
    <slot name="full">
      <div class="mx-100px w-full max-w-500px">
        <slot />
      </div>
    </slot>
  </div>
</div>
