<template>
  <ArrowUpRightIcon class="icon" />
</template>

<script>
import { ArrowUpRightIcon } from "@heroicons/vue/20/solid";

export default {
  name: "ArrowUpRight",
  components: {
    ArrowUpRightIcon,
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
