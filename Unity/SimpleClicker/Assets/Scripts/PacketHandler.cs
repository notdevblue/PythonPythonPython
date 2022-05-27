using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PacketHandler : MonoSingleton<PacketHandler>
{
    private Exception _keyNotFoundException;
    private Dictionary<string, Action<(List<string>, List<string>)>> _packetHandlerDictionary;

    private void Awake()
    {
        _keyNotFoundException = new Exception($"PacketHandler::Handle > key does not exist");
        _packetHandlerDictionary = new Dictionary<string, Action<(List<string>, List<string>)>>();
    }

    /// <summary>
    /// Handles Packet
    /// </summary>
    /// <param name="type">packet type</param>
    /// <param name="members">packet members</param>
    /// <exception cref="_keyNotFoundException"></exception>
    public void Handle(string type, (List<string>, List<string>) members)
    {
        Debug.Log(type);
        
        if(!_packetHandlerDictionary.ContainsKey(type)) {
            throw _keyNotFoundException;
        }


        _packetHandlerDictionary[type](members);
    }

    /// <summary>
    /// Adds packet handler
    /// </summary>
    /// <param name="type">type</param>
    /// <param name="callback">called when packet(type) arrived</param>
    public void AddHandler(string type, Action<(List<string>, List<string>)> callback)
    {
        if (_packetHandlerDictionary.ContainsKey(type))
        {
            _packetHandlerDictionary[type] += callback;
        }
        else
        {
            _packetHandlerDictionary.Add(type, callback);
        }
    }

}
