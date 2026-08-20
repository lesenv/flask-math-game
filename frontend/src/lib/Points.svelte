<script>
	let { points, attempts } = $props();
	let heart_string = $state("../../public/heart 2.jpg");
	let heart_grey_string = $state("../../public/heart 2-modified.jpg");
	
</script>

<div>Leben:
	<span>
    	{#each { length: points/10 }, count}
		    <img src={heart_string} width="{40+count*2}px" alt="O" />
		{/each}
		{#each {length: 10-points/10}, count}
			<img src={heart_grey_string} width="{40+(length-count)*2}px" alt="O" />
			{#if (count+1)%10==0} <br />{/if}
	    {/each}
		{#each { length: attempts }} <em>X</em>{/each}
    </span>
</div>