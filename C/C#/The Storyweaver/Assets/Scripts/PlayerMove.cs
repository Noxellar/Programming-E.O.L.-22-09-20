using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMove : MonoBehaviour
{
	// Player rigidbody variable declaration
	Rigidbody2D playerRigidbody;

	// Player Input Action variable declaration
	PlayerInputActions playerInputActions;

	// Movement Input variable declaration
	Vector2 movementInput;

	// Movement speed, jump height, and jumping status
	public float movementSpeed = 1f;
	public float jumpHeight = 200f;
	bool isJumping = false;

	void Awake()
	{
		// Player rigidbody variable assignment
		playerRigidbody = GetComponent<Rigidbody2D>();

		// Player input action variable assignment to input action maps called "Player Input Actions"
		playerInputActions = new PlayerInputActions();

		// .Player is a action map and .Move is an action
		playerInputActions.Player.Move.performed += ctx => movementInput = ctx.ReadValue<Vector2>();
	}

	void Update()
	{
		// Player x velocity. Time.deltaTime is not included because
		// movementSpeed is in already velocity: m/s
		Vector2 playerVelocityX = new Vector2(movementInput.x, 0);
		Vector2 playerVelocityY = transform.up * 0;

		if (!isJumping)
		{
			playerVelocityY = (transform.up * movementInput.y) * jumpHeight;
		}

		playerRigidbody.velocity = playerVelocityX + playerVelocityY;

		Debug.Log(playerVelocityX);
	}

	void OnCollisionStay2D(Collision2D collisionObject)
	{
		isJumping = false;
	}

	void OnCollisionExit2D(Collision2D collisionObject)
	{
		isJumping = true;
	}

	void OnEnable()
	{
		playerInputActions.Enable();
	}

	void OnDisable()
	{
		playerInputActions.Disable();
	}
}
