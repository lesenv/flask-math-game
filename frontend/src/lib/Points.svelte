<script>
	let { points } = $props();
</script>

<div>Leben: <span>
	{#each { length: points/10 }}<img src="../../public/heart 2.jpg" width="40px" alt="X" \>{/each}</span></div>