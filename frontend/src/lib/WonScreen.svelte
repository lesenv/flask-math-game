<script>
    import Confetti from 'svelte-confetti';
    import { user } from '../user.svelte';
	let { username } = $props();
</script>

<div>
	<h1>GEWONNEN!!</h1><Confetti xSpread={1} duration={5000} amount={100} />
	<h2>{user.username},<Confetti xSpread={1} duration={5000} amount={100} /> Du hast es geschafft!!</h2>
	<h2><Confetti xSpread={1} duration={5000} amount={100} />{user.points} Punkte hast Du Dir verdient!!<Confetti xSpread={1} duration={5000} amount={100} /></h2>
</div>
<Confetti 
  xSpread={1} 
  duration={5000} 
  amount={100} 
/>
<div id="leftie">
	Schön, dass Du wieder vorbeigeschaut hast!
</div>
<div id="andnow">
	Und jetzt kannst Du wieder springen, laufen, tanzen!<br />
	Alles gleichzeitig?
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
	#andnow {
		float: right;
		text-align: right;
		color: green;
		background-color: #eee;
		border-radius: 4em;
		padding: 4em;
	}
</style>