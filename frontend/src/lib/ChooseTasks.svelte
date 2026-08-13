<style>
    #ChoseTasksDiv {
      background-color: #eeeeee;
      padding: 2em;
      border-radius: 0em 2em 2em 0em;
    }
    #ChoseTasks {
      background-color: #dddddd;
      border-radius: 0em 2em 2em 0em;
      padding: 2em;
    }
    ul {
      list-style-type: none;
    }
</style>
<script>
    let { sidebar_tasks = [] } = $props()
</script>
<div id="ChoseTasksDiv">
  <form method="POST" action="?/checkboxes">
    <ul id="ChoseTasks">
      <li>""--{ sidebar_tasks }--""</li>
      {#each sidebar_tasks as task}
      <li><input type="checkbox" value="{task}"  /><label>{task}</label></li>
      {/each}
    </ul>
    	<button formaction="?/aktualisieren">Aktualisieren</button>
  </form>
</div>