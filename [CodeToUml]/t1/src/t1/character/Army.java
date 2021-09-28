package t1.character;


/**
*
* @author Leo lvcdb, Adrien G
*/

 class Army implements Character {

	protected  int size;

	protected  int MAX_SIZE;


	/**
	* //TODO
	*
	* @return :void:
	**/
 	public void Army(Tile position, Player owner, int size) ;

	/**
	* //TODO
	*
	* @return :int:
	**/
 	public int getSize() {

		return 0;
	}

	/**
	* //TODO
	*
	* @return :int:
	**/
 	public int numberUnitsClaimed() {

		return 0;
	}

	/**
	* //TODO
	*
	* @param other : Army: 
	*
	* @return :String:
	**/
 	public String meet(Army other) {

		return "";
	}

	/**
	* //TODO
	*
	* @param other : Army: 
	*
	* @return :String:
	**/
 	public String supportArmy(Army other) {

		return "";
	}

	/**
	* //TODO
	*
	* @param other : Army: 
	*
	* @return :String:
	**/
 	public String fight(Army other) {

		return "";
	}

	/**
	* //TODO
	*
	* @param owner : Player: 
	*
	* @return :void:
	**/
 	public void changeOwner(Player owner) ;

	/**
	* //TODO
	*
	* @return :void:
	**/
 	public void looseFight() ;

	/**
	* //TODO
	*
	* @return :void:
	**/
 	public void extendArmy() ;

	/**
	* //TODO
	*
	* @param newTile : Tile: 
	*
	* @return :void:
	**/
 	public void setTile(Tile newTile) ;

	/**
	* //TODO
	*
	* @param reward : int: 
	*
	* @return :void:
	**/
 	public void receiveReward(int reward) ;


}