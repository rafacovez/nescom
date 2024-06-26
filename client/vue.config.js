// load env vars
require("./loadEnvironment.js");

const { defineConfig } = require("@vue/cli-service");

module.exports = defineConfig({
  transpileDependencies: true,
});
