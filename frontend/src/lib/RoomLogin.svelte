<script>
  import { socketState } from '../socket.svelte';

  let { loggedUsers = $bindable(), onRemove, createNewUser } = $props(); 

  let username = $state("");
  let roomname = $state("");

  function submitLogin(name) {
    socketState.joinRoom(name, roomname);
  }

  function newUser() {
    let newUserName = document.getElementsByName("newUserName")[0].value;
    createNewUser(newUserName);
  }

  function handleSubmit(event) {
  	event.preventDefault();
  	socketState.joinRoom(username, roomname);
  }
</script>
<div style="margin: auto; width: 240px;">
    <div id="direct_login" style="padding: 1rem 0;">
        {#each loggedUsers.toSorted((a, b) => a.localeCompare(b)) as user}
        <div class="button-wrapper">
            <button type="button" class="main-button" onclick={() => submitLogin(user)}>{user}</button>
            <button type="button" class="remove-button" onclick={() => onRemove(user)}>X</button>
        </div>
        {/each}
        <form>
            <input name="newUserName"/><button type="submit" class="main-button" onclick={() => newUser()}>NEU</button>
        </form>
    </div>
</div>

<style>

input {
    display: inline;
}

.button-wrapper {
    position: relative;
    margin-bottom: 0.48rem;
  }

  .main-button {
    padding: 0.75rem 1.5rem;
  }

  .remove-button {
    position: absolute;
    top: -8px;
    right: -8px;

    width: 20px;
    height: 20px;
    padding: 0;

    border: none;
    border-radius: 50%;
    background: #e53935;
    color: white;

    cursor: pointer;
    font-size: 16px;
    line-height: 20px;
  }

  .remove-button:hover {
    background: #c62828;
  }

button {
    display: inline!important;
}

</style>