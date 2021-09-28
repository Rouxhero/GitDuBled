package t1.player;


/**
*
* @author Leo lvcdb, Adrien G
*/

 class WarPlayer implements Player {

	private  int gold;

	private  int nbSoldier;


	/**
	* //TODO
	*
	* @return :void:
	**/
 	public void WarPlayer(String name, Board board, boolean isRandom) ;

	/**
	* //TODO
	*
	* @param character : Character: 
	*
	* @return :void:
	**/
 	public void looseChar(Character character) ;

	/**
	* //TODO
	*
	* @return :int:
	**/
 	public int getNbSoldier() {

		return 0;
	}

	/**
	* //TODO
	*
	* @return :String:
	**/
 	public String deployCharact(int size, int x, int y) {

		return "";
	}

	/**
	* //TODO
	*
	* @return :int:
	**/
 	public int getGold() {

		return 0;
	}

	/**
	* //TODO
	*
	* @return :int:
	**/
 	public int getPoint() {

		return 0;
	}


}