abstract class Game {

	public List<Player> playerList;
	public int nbRound;
	public Board theBoard;
	public final int lastRound;
	/**
	* def
	* @return :int:
	**/
	public int getLastRound(){

		return 0;
	}

	/**
	* def
	* @return :void:
	**/
	public void addPlayer(Player player);

	/**
	* def
	* @return :void:
	**/
	public void playOnRound();

	/**
	* def
	* @return :void:
	**/
	public void play();


}