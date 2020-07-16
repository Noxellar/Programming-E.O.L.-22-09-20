using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMove : MonoBehaviour
{
	// Player rigidbody variable declaration
	Rigidbody2D playerRigidbody;

	// Movement speed, jump height, and jumping status
	public float movementSpeed = 500f;
	public float jumpHeight = 200f;
	bool isJumping = false;
	// Player Input Action variable declaration
	PlayerInputActions inputAction;

	// Movement Input variable declaration
	Vector2 movementInput;

	void Awake()
	{
		// Player rigidbody variable assignment
		playerRigidbody = GetComponent<Rigidbody2D>();

		// Player input action variable assignment to input action maps called "Player Input Actions"
		inputAction = new PlayerInputActions();

		// .Player is a action map and .Move is an action
		inputAction.Player.Move.performed += ctx => movementInput = ctx.ReadValue<Vector2>();
	}

	void Update()
	{
		Vector2 movement = playerRigidbody.velocity;

		float x = movementInput.x;
		float y = movementInput.y;

		movement.x = x * movementSpeed * Time.deltaTime;
		if (y != 0 && !isJumping)
		{
			movement.y = y * jumpHeight * Time.deltaTime;
		}

		playerRigidbody.velocity = movement;
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
		inputAction.Enable();
	}

	void OnDisable()
	{
		inputAction.Disable();
	}
}
