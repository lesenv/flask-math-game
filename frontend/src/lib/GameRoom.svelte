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
  <input type="number" name="inputText" bind:value={result} bind:this={inputRef} />
  <button type="submit" style="display: none;">Solve</button>
</form>
</div>
<style>
  form {
    background-color: #bbbbbb;
    padding: 2em;
    border-radius: 2em 0 0 2em;
  }
</style>