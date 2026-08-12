<script>
    let { sidebar_tasks = [] } = $props()
</script>
<div>
  <ul>
    <li>"Wann kommen alle Einträge? in ChooseTasks.svelte"</li>
    {#each sidebar_tasks as task}
    <li><option>{task}</option></li>
    {/each}
  </ul>
</div>