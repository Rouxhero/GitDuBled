package t1.gamemode;


/**
*
* @author Leo lvcdb, Adrien G
*/

abstract class Game implements Game {

	protected  Board theBoard;

	protected  List<Player> allPlayer;

	protected static  Random ALEA;

	protected  int nbRound;


	/**
	* //TODO
	*
	* @param nbRound : int: 
	*
	* @return :void:
	**/
 	public void Game(int nbRound) ;

	/**
	* //TODO
	*
	* @param thePlayer : Player: 
	*
	* @return :void:
	**/
 	public void addPlayer(Player thePlayer) ;

	/**
	* //TODO
	*
	* @return :List<Player>:
	**/
 	public List<Player> getPlayer() {

		return new List<Player>() ;
	}

	/**
	* //TODO
	*
	* @return :Board:
	**/
 	public Board getTheBoard() {

		return new Board() ;
	}

	/**
	* //TODO
	*
	* @return :int:
	**/
 	public int getNbRound() {

		return 0;
	}

	/**
	* //TODO
	*
	* @return :String:
	**/
 	public String play() {

		return "";
	}


}