<script>
  import { socketState } from '../socket.svelte';

  let { match } = $props();

  let result = $state();
  let inputRef = $state(null);

  function handleSubmit(event) {
  	event.preventDefault();
  	socketState.submitResults(result);
    result = null;
  }

  $effect(() => {
    inputRef?.focus();
  });

</script>
<div>
<form onsubmit={handleSubmit}>
  {match.task.str} = 
  <input type="number" bind:value={result} bind:this={inputRef} />
  <button type="submit" style="display: none;">Solve</button>
</form>
<ul>
  <li>poesjfdpm in GameRoom</li>
  <li>oihasdom</li>
</ul>
</div>
<style>
  div {
    background-color: #bbbbbb;
    padding: 2em
  }
</style>