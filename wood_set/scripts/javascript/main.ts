//Filename: main.ts
//Generated with StarkTMA/Anvil 1.0.1
//Time: 05-11-2026 17:55:09 +0100
//Property of Stark_As

import { system } from "@minecraft/server";
import { registerWoodSet } from "./blocks/wood_set";

system.beforeEvents.startup.subscribe((init) => {
	registerWoodSet(init);
});
