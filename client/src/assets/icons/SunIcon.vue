<template>
  <SunIcon class="icon" />
</template>

<script>
import { SunIcon } from "@heroicons/vue/20/solid";

export default {
  name: "SunIcon",
  components: {
    SunIcon,
  },
};
</script>

<style>
.icon {
  margin-left: 5px;
  width: 15px;
  transition: all ease-out 0.2s;
}

*:hover > .icon {
  transform: translate(5px, -5px);
}
</style>
