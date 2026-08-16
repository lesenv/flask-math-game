<script>
	import { socketState } from '../socket.svelte';

	let { enabled_tasks = $bindable() } = $props();
	let isDisabled = $derived.by(() => (
		!Object.values(enabled_tasks).some(value => value === true)
	));

	function handleSubmit(event) {
		event.preventDefault();
		socketState.updateTasks(enabled_tasks);
	}

</script>

<form onsubmit={handleSubmit} name="task-form">
	{#each Object.entries(enabled_tasks) as [task, enabled]}
		<div>
			<label>
				<input type="checkbox" bind:checked={enabled_tasks[task]} />
				{ task }
			</label>
		</div>
	{/each}
	<div>
		<button type="submit" disabled={isDisabled}>Update</button>
	</div>
</form>

<style>
	form[name="task-form"] {
		padding: 0.64rem;
	}

</style>