<script>
    import Confetti from 'svelte-confetti';
    import { user } from '../user.svelte';
    import { socketState } from '../socket.svelte';

	function resume_playing() {
		socketState.new_game()
	}
</script>

<div>
	<h1>GEWONNEN!!</h1>
	<h2>{user.username}, Du hast es geschafft!!</h2>
	<h2>{user.points} Punkte hast Du Dir verdient!!</h2>
</div>
<Confetti 
  xSpread={3} 
  duration={5000} 
  amount={100} 
/>
<div id="leftie">
	Schön, dass Du wieder vorbeigeschaut hast!
</div>
<div id="rightie">
	Und jetzt kannst Du wieder springen, laufen, tanzen!<br />
	Alles gleichzeitig?
</div>

<div>
	<form onsubmit={resume_playing} name="task-form">
		<button type="submit">WEITER BITTE</button>
	</form>
</div>

<style>
	div { text-align: center; }
	h1{ color: red; }
	h2 {color: blue;}
	#leftie { 
		float: left;
		text-align: left;
		color: #aaa;
		background-color: greenyellow;
		border-radius: 4em;
		padding: 4em;
	}
	#rightie {
		float: right;
		text-align: right;
		color: green;
		background-color: #eee;
		border-radius: 4em;
		padding: 4em;
	}
</style>