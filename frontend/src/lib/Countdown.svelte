<script>

	let { display } = $props();

    let count = $state(10);

    $effect(() => {
        if (count <= 0) return;

        const timeout = setTimeout(() => {
            count--;
        }, 1); //000); // was 1000 to count in seconds

        return () => clearTimeout(timeout);
    });
</script>

{#if count > 0}
   <h1>{count}</h1>
{:else}
   {@render display()}
{/if}
