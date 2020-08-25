using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.InputSystem;

public class CameraLook : MonoBehaviour
{
	// Player Transform variable declaration
	Transform playerTransform;

	// Player Rotation variable declaration
	Quaternion playerRotation;

	// Camera Transform variable declaration
	Transform cameraTransform;

	// Camera Rotation varaible declaration
	// Quaternion cameraRotation;

	// Look Sensitivity variable declaration
	float lookSensitivity;

	void Awake()
	{
		// Look Input and Look Sensitivity variable assignment
		lookSensitivity = 10;

		// Player Transform variable assignment
		playerTransform = GameObject.FindWithTag("Player").transform;

		// Player Rotation variable assignment
		playerRotation = playerTransform.rotation;

		// Camera Transform variable assignment
		cameraTransform = transform;

		// Camera Rotation variable assignment
		// cameraRotation = cameraTransform.rotation;

		Cursor.lockState = CursorLockMode.Locked;
		Cursor.visible = false;
	}

	public void Look(InputAction.CallbackContext ctx)
	{
		Vector2 lookInput = ctx.ReadValue<Vector2>();

		float playerRotationY = lookInput.x * lookSensitivity * Time.deltaTime;
		// playerRotation *= Quaternion.Euler(0, playerRotationY, 0);
		playerTransform.Rotate(0, playerRotationY, 0, Space.Self);

		float cameraRotationX = lookInput.y * lookSensitivity * Time.deltaTime;
		// cameraRotation *= Quaternion.Euler(cameraRotationX, 0, 0);
		cameraTransform.Rotate(-cameraRotationX, 0, 0, Space.Self);
	}
}
