using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraFollow : MonoBehaviour
{
	// Player transform variable declaration
	public Transform playerTransform;

	void Awake()
	{
		playerTransform = GameObject.FindGameObjectWithTag("Player").transform;
	}

	// LateUpdate() runs after every Update()
	// We use this so that this code doesn't run before the player moves
	// Fixes camera lagging behind the player
	void LateUpdate()
	{
		// Cameras current position
		Vector3 transformVector = transform.position;

		// Assigning new camera position
		transformVector.x = playerTransform.position.x;
		transformVector.y = playerTransform.position.y;

		// Assigning new camera position to camera object
		transform.position = transformVector;

		/*
			* Ok, this small piece of code might seem very confusing
			* Basically, transformVector is set to the camera's current position (2D vector form)
			* Then we manipulate that vector to the player's new position
			* But this does not change the camera's position
			* This is because it is it's own variable and is not the camera variable
			* So the last line of code makes the camera vector equal to the "new" vector
		*/
	}
}
