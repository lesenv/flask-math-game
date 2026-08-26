<script>
	let { points, attempts } = $props();
	let heart_string = $state("../../public/heart 2.jpg");
	let heart_grey_string = $state("../../public/heart 2-modified.jpg");
	let heart_string_2 = $state("../../public/heart 4.png");
	
</script>

<div>Leben:
	<span>
    	{#each { length: (points/10)%10 }, count}
		    <img src={heart_string} width="{40+count*2}px" alt="O" />
		{/each}
		{#each {length: 10-(points/10)%10}, count}
			<img src={heart_grey_string} width="{40+(length-count)*2}px" alt="o" />
	    {/each}
		{#each { length: attempts }} <em>X</em>{/each}
		{#if points>100}
			<img src={heart_string_2} width="40px" alt="100P" />x{Math.floor(points/100)}
		{/if}
    </span>
</div>