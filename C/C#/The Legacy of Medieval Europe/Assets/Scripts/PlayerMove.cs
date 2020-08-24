using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.InputSystem;

public class PlayerMove : MonoBehaviour
{
	// Player Input Action variable declaration
	public PlayerInputActions playerInputActions;

	// Player rigidbody variable declaration
	Rigidbody playerRigidbody;

	// Movement Input variable declaration
	Vector2 movementInput;

	// Movement Speed variable declaration
	public float movementSpeed;

	void Awake()
	{
		// Player input action variable assignment to input action maps called "Player Input Actions"
		playerInputActions = new PlayerInputActions();

		// .Player is the action map and .Move is the action
		playerInputActions.Player.Move.performed += ctx => movementInput = ctx.ReadValue<Vector2>();

		// Player rigidbody variable assignment
		playerRigidbody = GetComponent<Rigidbody>();

		// Movement Speed variable assignment in m/s
		movementSpeed = 3f;
	}

	public void Update()
	{
		// Player x and y velocities. Time.deltaTime is not included because
		// movementSpeed is in already velocity: m/s
		Vector3 playerVelocityX = (transform.right * movementInput.x) * movementSpeed;
		Vector3 playerVelocityY = (transform.forward * movementInput.y) * movementSpeed;

		playerRigidbody.velocity = playerVelocityX + playerVelocityY;
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
