package bku.iot.demoiot;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

import com.github.angads25.toggle.interfaces.OnToggledListener;
import com.github.angads25.toggle.model.ToggleableView;
import com.github.angads25.toggle.widget.LabeledSwitch;

import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallbackExtended;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;

import java.nio.charset.Charset;
import java.util.ArrayList;
import java.util.Locale;

import android.app.Activity;
import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.os.Bundle;
import android.speech.RecognizerIntent;
import android.view.Menu;
import android.view.View;
import android.widget.ImageButton;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    private TextView txtSpeechInput;
    private ImageButton btnSpeak;
    private final int REQ_CODE_SPEECH_INPUT = 100;

    MQTTHelper mqttHelper;
    TextView txtTemp,txtHumi,txtLight,txtMoisture;
    LabeledSwitch btnLED, btnPUMP, btnAI;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        txtSpeechInput = findViewById(R.id.txtSpeechInput);
        btnSpeak = findViewById(R.id.btnSpeak);
        txtTemp = findViewById(R.id.txtTemperature);
        txtHumi = findViewById(R.id.txtHumidity);
        txtMoisture = findViewById(R.id.txtMoisture);
        txtLight = findViewById(R.id.txtLight);
        btnLED = findViewById(R.id.btnLED);
        btnPUMP = findViewById(R.id.btnPUMP);
        btnAI = findViewById(R.id.btnAI);

        btnLED.setOnToggledListener(new OnToggledListener() {
            @Override
            public void onSwitched(ToggleableView toggleableView, boolean isOn) {
                if(isOn==true){
                    sendDataMQTT("CaptainCuong/feeds/nutnhan1", "1");
                }else{
                    sendDataMQTT("CaptainCuong/feeds/nutnhan1", "0");
                }
            }
        });
        btnPUMP.setOnToggledListener(new OnToggledListener() {
            @Override
            public void onSwitched(ToggleableView toggleableView, boolean isOn) {
                if(isOn==true){
                    sendDataMQTT("CaptainCuong/feeds/nutnhan2", "1");
                }else{
                    sendDataMQTT("CaptainCuong/feeds/nutnhan2", "0");
                }
            }
        });
        btnSpeak.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                promptSpeechInput();
            }
        });
        btnAI.setOnToggledListener(new OnToggledListener() {
            @Override
            public void onSwitched(ToggleableView toggleableView, boolean isOn) {
                if(isOn==true){
                    sendDataMQTT("CaptainCuong/feeds/detect-mask", "1");
                }else{
                    sendDataMQTT("CaptainCuong/feeds/detect-mask", "0");
                }
            }
        });
        startMQTT();
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        switch (requestCode) {
            case REQ_CODE_SPEECH_INPUT: {
                if (resultCode == RESULT_OK && null != data) {
                    ArrayList<String> result = data
                            .getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS);
                    txtSpeechInput.setText(result.get(0));
                    if (result.get(0).contains("lights on")){
                        sendDataMQTT("CaptainCuong/feeds/nutnhan1", "1");
                        btnLED.setOn(true);
                    }
                    if (result.get(0).contains("lights off")){
                        sendDataMQTT("CaptainCuong/feeds/nutnhan1", "0");
                        btnLED.setOn(false);
                    }
                    if (result.get(0).contains("pump on")){
                        sendDataMQTT("CaptainCuong/feeds/nutnhan2", "1");
                        btnPUMP.setOn(true);
                    }
                    if (result.get(0).contains("pump off")){
                        sendDataMQTT("CaptainCuong/feeds/nutnhan2", "0");
                        btnPUMP.setOn(false);
                    }
                }
                break;
            }
        }
    }

    private void promptSpeechInput() {
        Intent intent = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
        intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL,
                RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);
        intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, Locale.getDefault());
        intent.putExtra(RecognizerIntent.EXTRA_PROMPT,
                getString(R.string.speech_prompt));
        try {
            startActivityForResult(intent, REQ_CODE_SPEECH_INPUT);
        } catch (ActivityNotFoundException a) {
            Toast.makeText(getApplicationContext(),
                    getString(R.string.speech_not_supported),
                    Toast.LENGTH_SHORT).show();
        }
    }

    public void sendDataMQTT(String topic, String value){
        MqttMessage msg = new MqttMessage();
        msg.setId(1234);
        msg.setQos(0);
        msg.setRetained(false);

        byte[] b = value.getBytes(Charset.forName("UTF-8"));
        msg.setPayload(b);

        try {
            mqttHelper.mqttAndroidClient.publish(topic, msg);
        }catch (MqttException e){
        }
    }
    public void startMQTT(){
        mqttHelper = new MQTTHelper(this);
        mqttHelper.setCallback(new MqttCallbackExtended() {
            @Override
            public void connectComplete(boolean reconnect, String serverURI) {

            }

            @Override
            public void connectionLost(Throwable cause) {

            }

            @Override
            public void messageArrived(String topic, MqttMessage message) throws Exception {
                Log.d("TEST", topic + "***" + message.toString());
                if(topic.contains("cambien1")){
                    txtTemp.setText(message.toString() + "°C");
                }else if(topic.contains("cambien2")){
                    txtHumi.setText(message.toString() + "%");
                }else if(topic.contains("do_am")){
                    txtMoisture.setText(message.toString() + "%");
                }else if(topic.contains("anh_sang")){
                    txtLight.setText(message.toString() + "LUX");
                }else if(topic.contains("nutnhan1")){
                    if(message.toString().equals("1")){
                        btnLED.setOn(true);
                    }else{
                        btnLED.setOn(false);
                    }
                }else if(topic.contains("nutnhan2")){
                    if(message.toString().equals("1")){
                        btnPUMP.setOn(true);
                    }else{
                        btnPUMP.setOn(false);
                    }
                }
            }

            @Override
            public void deliveryComplete(IMqttDeliveryToken token) {

            }
        });
    }
}