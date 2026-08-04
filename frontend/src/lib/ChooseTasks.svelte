<script>
    let { sidebar_tasks } = $props()
</script>
<div>
    {#each sidebar_tasks as task}
    <li><option>{task}</option></li>
    {/each}
</div>