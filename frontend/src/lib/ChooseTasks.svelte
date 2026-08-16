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
    import { socketState } from "../socket.svelte";

    let { sidebar_tasks = [], sidebar_task_chosen = [] } = $props();

    function toggle_Checkbox(toggledTask) {
      socketState.toggleCheckbox(toggledTask);
    }

</script>
<div id="ChoseTasksDiv">
  <form method="POST" action="?/checkboxes">
    <ul id="ChoseTasks">
      <li>""--{ sidebar_tasks }--""</li>
      {#each sidebar_tasks as task, i}
      <li><label><input ontoggle={toggle_Checkbox(task)} type="checkbox" value="{task}" bind:group={sidebar_task_chosen} checked={sidebar_task_chosen[i]}/>{task}</label></li>
      {/each}
    </ul>
    <h3>{sidebar_task_chosen}</h3>
    	<button formaction="?/">Aktualisieren</button>
  </form>
</div>