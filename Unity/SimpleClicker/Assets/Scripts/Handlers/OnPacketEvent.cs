using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class OnPacketEvent : MonoBehaviour
{
    private void Start()
    {
        RequestSender.Instance.OnWebRequestArrived += PacketManager.Instance.ParsePacket;
        PacketManager.Instance.OnHandlePacket      += PacketHandler.Instance.Handle;
    }
}