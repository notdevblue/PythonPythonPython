using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;

public class RequestSender
{
   public string saveUrl = "http://localhost:48000/save";
   public string getUrl = "http://localhost:48000/get";

   public event Action OnWebRequestFailed;
   public event Action<string> OnWebRequestArrived;

   private static RequestSender _instance;
   public  static RequestSender Instance
   {
      get 
      {
         if (_instance == null)
            _instance = new RequestSender();

         return _instance;
      }
   }

   public IEnumerator SaveScore(string name, int score, Action<string> callback = null)
   {
      WWWForm form = new WWWForm();
      form.AddField("name", name);
      form.AddField("score", score);

      UnityWebRequest req = UnityWebRequest.Post(saveUrl, form);
      yield return req.SendWebRequest();

      switch (req.result)
      {
         case UnityWebRequest.Result.Success:
            callback?.Invoke(req.downloadHandler.text);
            OnWebRequestArrived?.Invoke(req.downloadHandler.text);
            break;

         default:
            Debug.LogError($"Request error > {req.result}\r\n{req.error}");
            callback?.Invoke(null);
            OnWebRequestFailed?.Invoke();
            break;
      }
   }

   public IEnumerator GetScore(string name, int range, Action<string> callback = null)
   {
      WWWForm form = new WWWForm();
      form.AddField("range", range);
      form.AddField("name", name);
      
      UnityWebRequest req = UnityWebRequest.Post(getUrl, form);
      yield return req.SendWebRequest();

      switch (req.result)
      {
         case UnityWebRequest.Result.Success:
            callback?.Invoke(req.downloadHandler.text);
            OnWebRequestArrived?.Invoke(req.downloadHandler.text);
            break;

         default:
            Debug.LogError($"Request error > {req.result}\r\n{req.error}");
            callback?.Invoke(null);
            OnWebRequestFailed?.Invoke();
            break;
      }
   }


}
