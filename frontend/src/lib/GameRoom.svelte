<script>
  import { socketState } from '../socket.svelte';

  let { match } = $props();

  let result = $state();
  let inputRef = $state(null);

  function handleSubmit(event) {
  	event.preventDefault();
  	socketState.submitResult(result);
    result = null;
  }

  $effect(() => {
    inputRef?.focus();
  });

</script>

<form onsubmit={handleSubmit}>
  {match.task.expr} = 
  <input type="text" bind:value={result} bind:this={inputRef} pattern="\s*[0-9]+(?:\s*/\s*[0-9]+)?\s*" />
  <button type="submit" style="display: none;">Solve</button>
</form>