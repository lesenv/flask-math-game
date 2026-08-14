import { socketState } from '../socket.svelte';

export const actions = {
	checkboxes: async (event) => {
        console.log("XXXXXXXXXCHECKER changed to ", event)
		socketState.submitChecker(event.value)
	},
	aktualisieren: async (event) => {
		let i = 2
	}
};

// when done with the checkers it's time for refactoring:

// cleaning up all the sidebars there are flying around everywhere
// just clear one after the other and testing if it still works

// get rid of all the errors when the website is getting in action