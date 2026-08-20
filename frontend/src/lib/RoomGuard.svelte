<script>
	let { join, open, close, won, joined = false, closed = false, won_bool = false } = $props();
</script>

{#if !joined}
	{@render join()}
{:else if won_bool}
    {@render won()}
{:else if joined && !closed}
	{@render open()}
{:else}
	{@render close()}
{/if}
