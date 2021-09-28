package t1.character;


/**
*
* @author Leo lvcdb, Adrien G
*/

abstract class Character {

	protected  int gold;

	protected  Player owner;

	protected  Tile position;


	/**
	* //TODO
	*
	* @return :void:
	**/
 	public void Character(Tile position, Player owner) ;

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
	* @return :int:
	**/
 	public int getGold() {

		return 0;
	}

	/**
	* //TODO
	*
	* @return :Tile:
	**/
 	public Tile getTile() {

		return new Tile() ;
	}

	/**
	* //TODO
	*
	* @return :Player:
	**/
 	public Player getOwner() {

		return new Player() ;
	}

	/**
	* //TODO
	*
	* @return :void:
	**/
 	public void kill() ;

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
	* @return :int:
	**/
 	public int numberUnitsClaimed() {

		return 0;
	}

	/**
	* //TODO
	*
	* @param pay : int: 
	*
	* @return :void:
	**/
 	public void addGold(int pay) ;

	/**
	* //TODO
	*
	* @return :String:
	**/
 	public String toString() {

		return "";
	}


}