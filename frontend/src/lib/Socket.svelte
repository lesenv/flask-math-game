<script>
  import { socketState } from '../socket.svelte';
  import { room } from '../room.svelte';
  import { user } from '../user.svelte';
  import RoomGuard from './RoomGuard.svelte'
  import RoomLogin from './RoomLogin.svelte'
  import Roster from './Roster.svelte';
  import Points from './Points.svelte';
  import GameRoom from './GameRoom.svelte'
  import Countdown from './Countdown.svelte'
  import TaskChooser from './TaskChooser.svelte';
  import { onMount } from 'svelte';
    import WonScreen from './WonScreen.svelte';

  let match = $state();
  let enabled_tasks = $state({}); 

  function leave() {
    socketState.leaveRoom();
    Object.assign(user, {});
  }

  onMount(() => {
    const socket = socketState.connect();

    socket.on("connect", () => {
        console.log("Verbunden:", socket.id);
    });

    const onRoom = (data) => {
        Object.assign(room, data);
        Object.assign(enabled_tasks, data.enabled_tasks);
    };

    socket.on("room", onRoom);

    const onUser = (data) => {
      console.log("data_user", data);
      Object.assign(user, data);
      Object.assign(room.members.find((item) => item.sid === data.sid) || {}, data);
    };

    socket.on("user", onUser);

    const onTask = (data) => {
      console.log("data_Task", data);
      match = data;
    };

    socket.on("task", onTask);


    return () => {
      socketState.leaveRoom();
      socket.off("room", onRoom);
      socket.off("user", onUser);
      socket.off("task", onTask);
      socketState.disconnect();
    };
  });

  $inspect(enabled_tasks);
</script>

<div>
  <RoomGuard joined={user.username} closed={room.state === 'closed'} won_bool={room.won === true}>
    {#snippet join()}
      <RoomLogin />
    {/snippet}
    {#snippet won()}
      <WonScreen username={user.name}/>
    {/snippet}
    {#snippet open()}
      <div class="main-layout">
        <div class="top-bar">
          <div class="spacer"></div>
          <div>Room: <span>{room.code}</span></div>
          <div><button type="button" onclick={ leave }>Leave</button></div>
        </div>
        <div class="main-container">
          <div class="sidebar">
            <Roster members={room.members} />
          </div>
          <div class="main-content">
            <p>Room is open. Waiting for members.</p>
          </div>
        </div>
      </div>        
    {/snippet}
    {#snippet close()}
      <div class="main-layout">
        <div class="top-bar">
          <Points points={ user.points } attempts = { match.attempts } />
          <div class="spacer"></div>
          <div>Room: <span>{room.code}</span></div>
          <div><button type="button" onclick={ leave }>Leave</button></div>
        </div>
        <div class="main-container">
          <div class="sidebar">
            <Roster members={room.members} />
          </div>
          <div class="main-content">
            {#if match}
              <Countdown>
                {#snippet display()}
                  <GameRoom match={match} />
                {/snippet}
              </Countdown>
            {/if}
          </div>
          <div class="sidebar sidebar-right">
            <TaskChooser bind:enabled_tasks={ enabled_tasks } />
          </div>
        </div>
      </div>
    {/snippet}
  </RoomGuard>
</div>

<style>

.main-layout {
	display: flex; 
	flex-direction: column;
	width: 100vw; 
	height: 100vh; 
}

.top-bar {
	flex-shrink: 0; 
	padding: 1.2rem 1rem; 
	border-bottom: 1px solid black;
	display: flex; 
	gap: 1rem;
}

.main-container {
	display: flex; 
	flex: 1;
}

.main-content {
	flex: 1;
	overflow-y: auto;
	display: flex;
	justify-content: center; 
	align-items: center; 
	height: 100%;
	box-sizing: border-box;
}

.sidebar {
	flex: 0 0 240px;
	overflow-y: auto;
	padding: 0;
	border-right: 1px solid black;
}

.sidebar-right {
  border-right: none;
  border-left: 1px solid black;
}

.spacer {
	flex-grow: 1;
}

.game-over {
	text-align: center;
	width: min(500px, 90%);
}

.results {
	margin: 1rem 0;
	border: 1px solid black;
	border-radius: 3px;
}

.result-row {
	display: flex;
	justify-content: space-between;
	padding: 0.64rem;
	border-bottom: 1px solid #ddd;
}

.result-row:last-child {
	border-bottom: none;
}

</style>