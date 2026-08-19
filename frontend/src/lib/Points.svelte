<script>
	let { points, attempts } = $props();
</script>

<div>Leben:
	<span>
    	{#each { length: points/10 }}<img src="../../public/heart 2.jpg" width="40px" alt="O" />{/each}
		{#each { length: attempts }} <em>X</em>{/each}
    </span>
</div>