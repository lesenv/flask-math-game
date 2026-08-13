<style>
    #ChoseTasksDiv {
      background-color: #eeeeee;
      padding: 2em;
    }
    #ChoseTasks {
      background-color: #dddddd;
    }
</style>
<script>
    let { sidebar_tasks = [] } = $props()
</script>
<div id="ChoseTasksDiv">
  <ul id="ChoseTasks">
    <li>"Wann kommen alle Einträge? in ChooseTasks.svelte"</li>
    <li>""--{ sidebar_tasks }--""</li>
    {#each sidebar_tasks as task}
    <li><option>{task}</option></li>
    {/each}
    <li>na hier drüber</li>
    <li>aoisjdom</li>
  </ul>
</div>