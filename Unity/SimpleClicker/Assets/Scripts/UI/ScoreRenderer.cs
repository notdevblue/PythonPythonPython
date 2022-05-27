using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ScoreRenderer : MonoBehaviour
{
   public static ScoreRenderer Instance;
   public Text text;

   private void Awake()
   {
      Instance = this;
   }

   private void Start()
   {
      UpdateText();
   }

   public void UpdateText()
   {
      text.text = $"당신은 이 고양이를 {GameManager.Instance.Score} 번 눌렀습니다.";
   }
}
