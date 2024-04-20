var HelloWorld=artifacts.require ("supply.sol");
module.exports = function(deployer) {
      deployer.deploy(HelloWorld);
}