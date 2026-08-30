<script>
    import Confetti from 'svelte-confetti';
    import { user } from '../user.svelte';
    import { socketState } from '../socket.svelte';

	function resume_playing() {
		socketState.resume_game_after_won()
	}

    let el = document.querySelector("btn_resume");
	console.log(el);
	el.focus();
</script>

<div>
	<h1>GEWONNEN!!</h1>
	<h2>{user.username}, Du hast es geschafft!!</h2>
	<h2>{user.points} Punkte hast Du Dir verdient!!</h2>
</div>
<Confetti 
  xSpread={8} 
  duration={5000} 
  amount={1000} 
/>
<div id="leftie">
	Schön, dass Du wieder vorbeigeschaut hast!<br />

	<button onclick={resume_playing} class="btn_resume">WEITER BITTE</button>
</div>
<div id="rightie">
	Und jetzt kannst Du wieder springen, laufen, tanzen!<br />
	Alles gleichzeitig?
</div>

<div>
</div>

<style>
	div { text-align: center; }
	h1{ color: red; }
	h2 {color: blue;}
	#leftie { 
		float: left;
		text-align: center;
		vertical-align: bottom;
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