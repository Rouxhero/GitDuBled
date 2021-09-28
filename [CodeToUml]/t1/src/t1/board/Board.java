package t1.board;


/**
*
* @author Leo lvcdb, Adrien G
*/

abstract class Board implements Board {

	protected  Tile[][] board;

	protected  List<Tile> allGround;


	/**
	* //TODO
	*
	* @return :void:
	**/
 	public void Board(int witdh, int height) ;

	/**
	* //TODO
	*
	* @param nbFirstTile : int: 
	*
	* @return :int:
	**/
 	public int getNbOfTile(int nbFirstTile) {

		return 0;
	}

	/**
	* //TODO
	*
	* @return :int:
	**/
 	public int getHeight() {

		return 0;
	}

	/**
	* //TODO
	*
	* @return :int:
	**/
 	public int getWitdh() {

		return 0;
	}

	/**
	* //TODO
	*
	* @return :void:
	**/
 	private void generateBoard() ;

	/**
	* //TODO
	*
	* @return :void:
	**/
 	private void genertateOcean() ;

	/**
	* //TODO
	*
	* @return :void:
	**/
 	private void generateFirstTile() ;

	/**
	* //TODO
	*
	* @param nbOfTile : int: 
	*
	* @return :void:
	**/
 	private void generateOtherTiles(int nbOfTile) ;

	/**
	* //TODO
	*
	* @return :boolean:
	**/
 	private boolean checkValidity(int posX, int posY) {

		return new boolean() ;
	}

	/**
	* //TODO
	*
	* @return :Tile:
	**/
 	private Tile createTile(int nb, int x, int y) {

		return new Tile() ;
	}

	/**
	* //TODO
	*
	* @return :List<Tile>:
	**/
 	public List<Tile> getAllFreeGround() {

		return new List<Tile>() ;
	}

	/**
	* //TODO
	*
	* @param tile : Tile: 
	*
	* @return :void:
	**/
 	public void removeOccupedGround(Tile tile) ;

	/**
	* //TODO
	*
	* @return :int:
	**/
 	public int getBoardStatus() {

		return 0;
	}

	/**
	* //TODO
	*
	* @return :String:
	**/
 	public String showBoard() {

		return "";
	}

	/**
	* //TODO
	*
	* @param widht : int: 
	*
	* @return :String:
	**/
 	private String generateHead(int widht) {

		return "";
	}

	/**
	* //TODO
	*
	* @param y : int: 
	*
	* @return :String:
	**/
 	private String getStr(int y) {

		return "";
	}

	/**
	* //TODO
	*
	* @return :Tile:
	**/
 	public Tile getTile(int x, int y) {

		return new Tile() ;
	}

	/**
	* //TODO
	*
	* @param tile : Tile: 
	*
	* @return :List<Tile>:
	**/
 	public List<Tile> getOtherTile(Tile tile) {

		return new List<Tile>() ;
	}


}