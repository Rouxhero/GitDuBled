package t1.tile;


/**
*
* @author Leo lvcdb, Adrien G
*/

abstract class Tile {

	public  Ressources HARVEST_RES;

	protected  int x;

	protected  int y;

	protected  String STRING_PICT;

	protected  boolean isEmpty;

	protected  Character user;


	/**
	* //TODO
	*
	* @return :void:
	**/
 	public void Tile(int x, int y) ;

	/**
	* //TODO
	*
	* @return :int:
	**/
 	public int getX() {

		return 0;
	}

	/**
	* //TODO
	*
	* @return :int:
	**/
 	public int getY() {

		return 0;
	}

	/**
	* //TODO
	*
	* @return :boolean:
	**/
 	public boolean isEmpty() {

		return new boolean() ;
	}

	/**
	* //TODO
	*
	* @return :Character:
	**/
 	public Character getUser() {

		return new Character() ;
	}

	/**
	* //TODO
	*
	* @param user : Character: 
	*
	* @return :void:
	**/
 	public void setUser(Character user) ;

	/**
	* //TODO
	*
	* @return :void:
	**/
 	public void leaveChar() ;


}