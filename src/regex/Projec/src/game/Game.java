package game.game;


abstract class Game implement Game  {

	public    List<Player> playerList;

	public    int nbRound;

	public    Board theBoard;

	public  final  int lastRound;


	/**
	* auto gen docs
	* @return :int:
	**/
 	public  int  getLastRound() {

		return 0;
	}

	/**
	* auto gen docs
	* @return :void:
	**/
 	public  void  addPlayer(Player player) ;

	/**
	* auto gen docs
	* @return :void:
	**/
 	public  void  playOnRound() ;

	/**
	* auto gen docs
	* @return :void:
	**/
 	public  void  play() ;


}